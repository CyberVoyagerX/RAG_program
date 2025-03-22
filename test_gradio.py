import gradio as gr

def greet(name, intensity):
    return "Hello, " + name + "!" * int(intensity)

# fn:包装界面的函数
# inputs：输入框
# outputs：输出框

demo = gr.Interface(
    fn=greet,
    inputs=["text", "slider"],
    outputs=["text"],
)

demo.launch()
