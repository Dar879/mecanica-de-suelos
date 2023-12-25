
import dearpygui.dearpygui as dpg




dpg.create_context()

dpg.create_viewport()

dpg.setup_dearpygui()



with dpg.window(label="Example Window"):

    dpg.add_text("Relaciones volumetricas y gravimetricas")

    dpg.add_input_text(label="string")
    dpg.add_input_text(label="la")
    dpg.add_input_text(label="casa")
    dpg.add_input_text(label="de los gritos")
    dpg.add_button(label="alskjdawdilawd button")
    dpg.add_slider_float(label="float")



dpg.show_viewport()

dpg.start_dearpygui()

dpg.destroy_context()