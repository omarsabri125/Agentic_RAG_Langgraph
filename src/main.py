from dotenv import load_dotenv
load_dotenv()
import pprint
from graph.workflow import create_workflow

if __name__ == "__main__":

    app = create_workflow()
    inputs = {
        "query":
            "What are the types of agent memory?"
    }
    for output in app.stream(inputs):
        for key, value in output.items():
            pprint.pprint(f"Output from node '{key}':")
            pprint.pprint("---")
            pprint.pprint(value, indent=2, width=80, depth=None)
        pprint.pprint("\n---\n")

