from typing import List
from pylsp import hookimpl
from pylsp.config.config import Config
from pylsp.workspace import Workspace, Document
from . import cfg
import logging

logname = "/tmp/manthan-adop-test.log"
logging.basicConfig(filename=logname,
                    filemode='w',
                    force=True,
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%Y/%m/%d %H:%M:%S',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


@hookimpl
def pylsp_settings():
    logger.info("Initializing test plugin")
    return {
        "plugins": {},
    }


@hookimpl
def pylsp_execute_command(config: Config, workspace: Workspace, command: str, arguments: List[str]):
    logger.info("workspace/executeCommand: %s %s", command, arguments)

    if command == "manthan.show_hello_world":
        logger.info("Called manthan.show_hello_world")
        doc_uri = arguments[0]
        document = workspace.get_document(doc_uri)
        execute_run_scan(config, workspace, document)


def execute_run_scan(config: Config, workspace: Workspace, document: Document):
    cfg.diagnostics[document.uri] = [
        {
            "uri": document.uri,
            "source": "adop",
            "range": {
                "start": {
                    "line": 1,
                    "character": 4,
                },
                "end": {
                    "line": 2,
                    "character": 4,
                },
            },
            "severity": 1
        }
    ]
    workspace.publish_diagnostics(
        doc_uri=document.uri, diagnostics=cfg.diagnostics.get(document.uri))
