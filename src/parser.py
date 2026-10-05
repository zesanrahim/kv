from kv import KVStore


class CommandParser:
    """Turns a line of text like 'PUT name Zesan' into a KVStore call and a reply string."""

    def __init__(self, store: KVStore) -> None:
        self.store = store

    def handle(self, line: str) -> str:

        parts = line.strip().split(" ", 2)
        command = parts[0].upper()
        args = parts[1:]

        if command == "GET":
            if len(args) != 1:
                return "ERROR usage: GET key"
            try:
                return f"VALUE {self.store.get(args[0])}"
            except KeyError:
                return "NOT_FOUND"

        if command == "PUT":
            if len(args) != 2:
                return "ERROR usage: PUT key value"
            self.store.put(args[0], args[1])
            return "OK"

        if command == "DELETE":
            if len(args) != 1:
                return "ERROR usage: DELETE key"
            return "OK" if self.store.delete(args[0]) else "NOT_FOUND"

        if command == "":
            return "ERROR empty command"

        return f"ERROR unknown command {command}"
