
ipc_sendfd_function = {
    "name": "ipc_sendfd",
    "topic": "ipc",
    "info": "sends a file descriptor over IPC connection",

    "result": {
        "type": "int",
        "success": "0",
        "error": "-1",
    },
    "args": [
        {
            "name": "s",
            "type": "int",
            "info": "IPC connection handle.",
        },
        {
            "name": "fd",
            "type": "int",
            "info": "The OS-level file descriptor to send.",
        },
    ],

    "prologue": """
        This function sends an OS-level file descriptor via IPC connection.
        Use ipc_recvfd to retrieve the file descriptor in the destination
        process.

        Technically, the file descriptor is sent via SCM_RIGHTS option.
        The descriptor is attached to a message 1 byte long.
    """,

    "has_deadline": True,
}

new_function(ipc_sendfd_function)

