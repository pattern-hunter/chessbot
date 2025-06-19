from temporalio import activity
from dataclasses import dataclass

@dataclass
class ComposeGreetingInput:
    greeting: str
    name: str

# Basic activity that logs and does string concatenation
@activity.defn
async def compose_greeting(input: ComposeGreetingInput) -> str:
    activity.logger.info("Running activity with parameter %s" % input)
    return f"{input.greeting}, {input.name}!"