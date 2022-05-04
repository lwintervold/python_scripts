import cProfile
import functools
import io
import pstats


def performance_reporter(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        profile = cProfile.Profile()
        profile.enable()

        func(*args, **kwargs)

        profile.disable()
        stream = io.StringIO()
        stats = pstats.Stats(profile, stream=stream).sort_stats('cumtime')
        stats.print_stats()
        with open('./perf', 'w') as file:
            file.write(stream.getvalue())

    return wrapper
