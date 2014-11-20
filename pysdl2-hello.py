import os
import sys
os.environ["PYSDL2_DLL_PATH"] = "c:\\python34"
import sdl2.ext

RESOURCES = sdl2.ext.Resources(__file__, "resources")

sdl2.ext.init()

window = sdl2.ext.Window("Hello World!",size=(640,480))
window.show()

factory = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)
sprite = factory.from_image(RESOURCES.get_path("diamond.bmp"))

spriterender = factory.create_sprite_render_system(window)
spriterender.render(sprite)

processor = sdl2.ext.TestEventProcessor()
processor.run(window)

sdl2.ext.quit()
