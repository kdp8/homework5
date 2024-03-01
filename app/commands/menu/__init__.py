from app.commands import CommandHandler


class MenuCommand(CommandHandlerhandler):
    def execute(self):
        print("This program consists of the following commands: ")
        CommandHandler.print_commands()