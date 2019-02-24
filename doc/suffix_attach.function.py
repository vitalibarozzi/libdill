
suffix_attach_function = {
    "name": "suffix_attach",
    "topic": "suffix",
    "info": "creates SUFFIX protocol on top of underlying socket",
    "result": {
        "type": "int",
        "success": "newly created socket handle",
        "error": "-1",
    },
    "args": [
       {
           "name": "s",
           "type": "int",
           "info": "Handle of the underlying socket. It must be a " +
                 "bytestream protocol.",
       },
       {
           "name": "suffix",
           "type": "const void*",
           "info": "The delimiter byte sequence.",
       },
       {
           "name": "suffixlen",
           "type": "size_t",
           "info": "The size of the delimiter, in bytes.",
       },
       {
           "name": "opts",
           "type": "const struct suffix_opts*",
           "dill": True,
           "info": "Options.",
       },
    ],

    "prologue": """
        This function instantiates SUFFIX protocol on top of the underlying
        protocol.
    """,
    "epilogue": """
        The socket can be cleanly shut down using **suffix_detach** function.
    """,
    "has_handle_argument": True,
    "allocates_handle": True,
    "mem": "suffix_storage",
    "custom_errors": {
        "EPROTO": "Underlying socket is not a bytestream socket.",
    },
}

new_topic(suffix_attach_function)

