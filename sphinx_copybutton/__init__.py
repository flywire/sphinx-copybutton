"""A small sphinx extension to add "copy" buttons to code blocks."""
import os

__version__ = "0.2.9dev0"

def scb_static_path(app):
    static_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '_static'))
    app.config.html_static_path.append(static_path)

def add_to_context(app, config):
    # Update the global context
    config.html_context.update({'copybutton_prompt_text': config.copybutton_prompt_text})
    config.html_context.update({'copybutton_only_copy_prompt_lines': config.copybutton_only_copy_prompt_lines})
    config.html_context.update({'copybutton_remove_prompts': config.copybutton_remove_prompts})
    config.html_context.update({'copybutton_image_path': config.copybutton_image_path})

def setup(app):
    print('Adding copy buttons to code blocks...')
    # Add our static path
    app.connect('builder-inited', scb_static_path)

    # configuration for this tool
    app.add_config_value("copybutton_prompt_text", ">>> ", "html")
    app.add_config_value("copybutton_only_copy_prompt_lines", True, "html")
    app.add_config_value("copybutton_remove_prompts", True, "html")
    app.add_config_value("copybutton_image_path", "copy-button.svg", "html")

    # Add configuration value to the template
    app.connect("config-inited", add_to_context)

    # Add relevant code to headers
    app.add_css_file('copybutton.css')
    app.add_js_file('clipboard.min.js')
    app.add_js_file("copybutton.js")
    return {"version": __version__,
            "parallel_read_safe": True,
            "parallel_write_safe": True}
