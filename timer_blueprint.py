import azure.functions as func
import logging
import datetime

blueprint = func.Blueprint()

@blueprint.function_name(name="TimerTriggerExample")
@blueprint.schedule(schedule="0 */5 * * * *",
                arg_name="mytimer",
                run_on_startup=True,
                use_monitor=False)
def log_timestamp(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()
    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)
