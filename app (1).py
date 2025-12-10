# CISC-121 Project: Binary Search Implementation 
# Author: Ikjot Bakshi 
# Date: 12/9/2025
# Professor: Ruslan Kain
def binary_search(a, target):
    '''
    Binary Search Implementation
    Returns index of target in a if found else returns -1
    '''
    # low starts at the beginning of the list
    low = 0
    # high starts at the end of the list
    high = len(a) - 1
    steps = []

    # search what side the target is on
    while low <= high:
        mid = (low + high) // 2
        # step for image for gradio
        steps.append({
            "low": low,
            "mid": mid,
            "high": high,
            "comparison": a[mid]
        })
        # if the middle value is the target return the index
        if a[mid] == target:
            return mid, steps
        # if the target is larger search the right side
        elif a[mid] < target:
            low = mid + 1
        # if the target is smaller search the left side
        else:
            high = mid - 1
    # if the loop ends and the target is not found within the list return -1 and end the steps
    return -1, steps





    
import gradio as gr
def run_binary_search(list_input, target_value):
    try:
        numbers = [int(x.strip()) for x in list_input.split(",") if x.strip() != ""]
        target = int(target_value)
    except ValueError:
        return "Error: enter integers only.", ""

    numbers.sort()
    index, steps = binary_search(numbers, target)

    step_lines = []
    for i, s in enumerate(steps):
        line = (
            f"Step {i+1}: "
            f"low = {s['low']}, "
            f"mid = {s['mid']} (value {s['comparison']}), "
            f"high = {s['high']}"
        )
        step_lines.append(line)

    if index == -1:
        result = f"Target {target} not found in {numbers}."
    else:
        result = f"Target {target} found at index {index} in {numbers}."

    return result, "\n".join(step_lines)
with gr.Blocks(title="Binary Search Implementation") as demo:
    gr.Markdown("# Binary Search Implementation")   # title
    gr.Markdown("# By: Ikjot Bakshi")   # author

    list_box = gr.Textbox(label="List (comma-separated)")     # subtext and textbox
    target_box = gr.Textbox(label="Target") # subtext and textbox

    submit_btn = gr.Button("Submit")   # submit button

    result_box = gr.Textbox(label="Result")     # subtext and textbox
    steps_box = gr.Textbox(label="Steps", lines=10)    # subtext and textbox

    submit_btn.click(
        run_binary_search,
        inputs=[list_box, target_box],
        outputs=[result_box, steps_box],
    )
if __name__ == "__main__":
    demo.launch()



