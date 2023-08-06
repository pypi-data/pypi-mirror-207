from .latex import LaTexParser, LaTexContext, Command, Scope, RequiredArgument, OptionalArgument, ArgumentSetting


def declare_constant(data_model, command):

    name = command.required_arguments[0]
    definition = command.required_arguments[1]

    data_model.define_constant(name, definition)


def declare_entrytypes(data_model, command):
    pass


def declare_fields(data_model, command):
    pass


def declare_entryfields(data_model, command):
    pass


def declare_constraints(data_model, command):
    pass


def reset_entrytypes(data_model, command):
    pass


def reset_fields(data_model, command):
    pass


def reset_entryfields(data_model, command):
    pass


def reset_constraints(data_model, command):
    pass


# noinspection SpellCheckingInspection
COMMAND_HANDLERS = {

    r'\DeclareDatamodelConstant': declare_constant,
    r'\DeclareDatamodelEntrytypes': declare_entrytypes,
    r'\DeclareDatamodelFields': declare_fields,
    r'\DeclareDatamodelEntryfields': declare_entryfields,
    r'\DeclareDatamodelConstraints': declare_constraints,
    r'\ResetDatamodelEntrytypes': reset_entrytypes,
    r'\ResetDatamodelFields': reset_fields,
    r'\ResetDatamodelEntryfields': reset_entryfields,
    r'\ResetDatamodelConstraints': reset_constraints
}


class DataModel(object):

    @property
    def constants(self):
        return self._constants

    @classmethod
    def from_file(self, filepath):

        unhandled_commands = []

        context = LaTexContext()

        parser = LaTexParser()
        result = parser.parse_file(filepath)

        for processable in result:

            element = processable.process(context)

            if isinstance(element, Command):

                handler = COMMAND_HANDLERS.get(element.identifier, None)

                if handler is None:
                    unhandled_commands.append(element)
                    continue

                handler(self, element)

            elif isinstance(element, Scope):
                pass

        pass

    def __init__(self):

        self._constants = {}

    def declare_constant(self, name, definition, options=None):
        pass

    def declare_entrytypes(self):
        pass

    def declare_fields(self):
        pass

    def declare_entryfields(self):
        pass

    def declare_constraints(self):
        pass

    def reset_entrytypes(self):
        pass

    def reset_fields(self):
        pass

    def reset_entryfields(self):
        pass

    def reset_constraints(self):
        pass

