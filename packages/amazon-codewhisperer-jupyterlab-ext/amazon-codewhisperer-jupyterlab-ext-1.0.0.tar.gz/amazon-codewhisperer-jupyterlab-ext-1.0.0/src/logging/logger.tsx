import pino from 'pino';

export class Logger {

  private static parentLogger: pino.Logger;


  public static getInstance(context?: Record<string, any>): pino.Logger {
    if (!Logger.parentLogger) {
      Logger.parentLogger = pino({
        level: 'error',
        prettyPrint: true,
      });
    }
    return this.parentLogger.child(context);
  }

  public static setLogLevel(level: string): void {
    Logger.parentLogger.level = level.toLowerCase();
  }
}

export default Logger;
