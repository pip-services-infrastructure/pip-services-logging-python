from pip_services_commons.log import ConsoleLogger
from pip_services_logging.container.LoggingProcess import LoggingProcess

if __name__ == '__main__':
    runner = LoggingProcess()
    try:
        runner.run_with_args()
    except Exception as ex:
        ConsoleLogger().fatal("logging", ex, "Error: ")
        #print(traceback.format_exc(ex))
        #sys.stderr.write(str(e) + '\n')