from pylsp import hookimpl

@hookimpl
def pylsp_lint(config, workspace, document, is_saved):
    return [{
        "source": "myextension",
        "message": "test",
        "range": {
            "start": {"line": 0, "character": 0},
            "end": {"line": 0, "character": 999},
        }
    }]
