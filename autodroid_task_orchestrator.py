import os
import time
from mobile_agent_benchmark.task_orchestrator import TaskOrchestrator

from droidbot import input_manager, env_manager
from container import orchestrator
from droidbot import DroidBot


def autodroid(prompt):

        # Define the task
        task = prompt
        print("task: ", task)

        # Define the APK path
        apk_path = "/Users/jonathanzha/Desktop/mobileAppapks/notes-fdroid-release.apk"

        # Define the device serial number
        device_serial = "emulator-5554"

        # Define the output directory
        output_dir = "bench_log"

        droidbot_instance = DroidBot(app_path=apk_path, device_serial=device_serial, task=task, output_dir=output_dir,env_policy=env_manager.POLICY_NONE,policy_name=input_manager.POLICY_TASK,random_input=True,event_count=10, timeout=-1, grant_perm=True, keep_app=True, keep_env=True)

        droidbot_instance.start()

        print("agent done")
if __name__ == "__main__":
    orchestrator.run(autodroid)
#     autodroid("open settings in this app")


