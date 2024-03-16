def init_mitsuba(RENDERER_cfgs):
    import mitsuba
    print(mitsuba.variants())
    print(f'set mitsuba variant as {RENDERER_cfgs.variant}')
    mitsuba.set_variant(RENDERER_cfgs.variant)
    if not RENDERER_cfgs.verbose:
        mitsuba.Thread.thread().logger().set_log_level(mitsuba.LogLevel.Warn)
