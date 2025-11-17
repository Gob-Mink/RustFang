# features/steps/sequencer_steps.py
from behave import when, then
import subprocess
@when('I press play')
def step_impl(context):
    context.result = subprocess.run(["./target/debug/rust_cli_poc", "play"], capture_output=True, text=True)
@then('I see the sequencer start')
def step_impl(context):
    assert "Sequencer started" in context.result.stdout
@when('I press stop')
def step_impl(context):
    context.result = subprocess.run(["./target/debug/rust_cli_poc", "stop"], capture_output=True, text=True)
@then('I see the sequencer stop')
def step_impl(context):
    assert "Sequencer stopped" in context.result.stdout