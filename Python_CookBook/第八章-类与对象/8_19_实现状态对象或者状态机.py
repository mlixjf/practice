class Connection:

    def __init__(self):
        self.new_state(ClosedConnectionState)

    def new_state(self, newstate):
        self._state = newstate

    def close(self):
        return self._state.close(self)

    def open(self):
        return self._state.open(self)

    def read(self):
        return self._state.read(self)

    def write(self, data):
        return self._state.write(self, data)


class ConnectionState:

    @staticmethod
    def close(conn):
        raise NotImplementedError("Not Implemented!")

    @staticmethod
    def open(conn):
        raise NotImplementedError("Not Implemented!")

    @staticmethod
    def read(conn):
        raise NotImplementedError("Not Implemented!")

    @staticmethod
    def write(conn, data):
        raise NotImplementedError("Not Implemented!")


class ClosedConnectionState(ConnectionState):

    @staticmethod
    def close(conn):
        raise RuntimeError("Already closed")

    @staticmethod
    def open(conn):
        conn.new_state(OpenedConnectionState)

    @staticmethod
    def read(conn):
        raise NotImplementedError("Not open")

    @staticmethod
    def write(conn, data):
        raise NotImplementedError("Not open")


class OpenedConnectionState(ConnectionState):

    @staticmethod
    def close(conn):
        conn.new_state(ClosedConnectionState)

    @staticmethod
    def open(conn):
        raise RuntimeError("Already open!")

    @staticmethod
    def read(conn):
        print("Reading")

    @staticmethod
    def write(conn, data):
        print("Writing", data)


if __name__ == '__main__':
    c = Connection()
    print(c._state)
    c.open()
    c.close()