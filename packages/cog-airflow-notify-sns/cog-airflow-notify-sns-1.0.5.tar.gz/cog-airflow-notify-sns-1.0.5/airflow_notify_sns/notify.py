import logging
from datetime import datetime

LOGGING = logging.getLogger(__name__)

from airflow.models.variable import Variable
from airflow.providers.amazon.aws.hooks.base_aws import AwsBaseHook


class Notify:

    def __init__(
        self,
        aws_sns_topic_arn: str,
        airflow_url: str
    ):
        """
        params:
            aws_sns_topic_arn: AWS SNS topic ARN where airflow send error messages
            airflow_url: AWS load balancer DNS by airflow
        """

        self.aws_sns_topic_arn = aws_sns_topic_arn
        self.airflow_url = airflow_url


    def _format_message_text(self, context):
        """
        Function to format airflow message

        params:
            context:  Airflow task execution context

        return:
            Message error formated
        """
        
        url = context.get('task_instance').log_url
        return """Airflow task execution failed. 
        *Time*: {time}  
        *Task*: {task}  
        *Dag*: {dag} 
        *Execution Time*: {exec_date}  
        *Log Url*: {log_url} 
        """.format(
            time=datetime.now(),
            task=context.get('task_instance').task_id,
            dag=context.get('task_instance').dag_id,
            ti=context.get('task_instance'),
            exec_date=context.get('execution_date'),
            log_url=url.replace("localhost:8080", self.airflow_url),
        )


    def send(self, context):
        """ 
        Publish Airflow Error Notification to a SNS Topic

        Parameters:
            context: Airflow task execution context
        
        Returns:
            boto3 sns_client.publish() response
        """

        sns_client = AwsBaseHook(client_type="sns", aws_conn_id='aws_default')

        # Message attributes
        subject = "ERROR - Airflow task execution failed"
        message = self._format_message_text(context)

        # Sending message to topic
        LOGGING.info(f"Error message to send: {message}")
        LOGGING.info(f"Sending error message to SNS Topic ARN [{self.aws_sns_topic_arn}]")
        try:
            response = sns_client.get_conn().publish(
                TopicArn=self.aws_sns_topic_arn,
                Subject=subject,
                Message=message
            )
            LOGGING.info("Message successfully sent do SNS Topic")
            return response
        except Exception as ex:
            LOGGING.error(f"Error sending message to SNS: [{ex}]")
            return None

        return None


def airflow_notify_sns(context, **kwargs):
    alerts_config = Variable.get('airflow_alerts_config', deserialize_json=True)
    
    # Make variable required
    if not alerts_config:
        LOGGING.error("Variable [airflow_alerts_config] not found in Airflow")
        return None

    sns_topic_arn = alerts_config.get('sns_topic_arn')
    airflow_url = alerts_config.get('airflow_url')
    
    notification = Notify(
        aws_sns_topic_arn = sns_topic_arn,
        airflow_url = airflow_url
    )
    notification.send(context)
