def on_a_pressed():
    music.play(music.create_sound_effect(WaveShape.SINE,
            5000,
            5000,
            255,
            0,
            500,
            SoundExpressionEffect.NONE,
            InterpolationCurve.LINEAR),
        music.PlaybackMode.UNTIL_DONE)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)
