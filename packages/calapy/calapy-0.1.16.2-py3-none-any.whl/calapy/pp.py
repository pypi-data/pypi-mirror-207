
import concurrent.futures as cf
# import os

__all__ = ['run']


def run(func, args=None, kwargs=None, n_workers=None):

    if args is None:
        args = ((),)
        n_elements_in_args = 1
    else:
        try:
            n_elements_in_args = len(args)
        except TypeError:
            raise ValueError('args must be an iterable of an iterable')

        for i in range(0, n_elements_in_args, 1):
            if args[i] is None:
                args[i] = ()
            else:
                try:
                    len(args[0])
                except TypeError:
                    raise ValueError('args must be an iterable of an iterable')

    if kwargs is None:
        n_elements_in_kwargs = 1
        kwargs = ({},)
    else:
        try:
            n_elements_in_kwargs = len(kwargs)
        except TypeError:
            raise ValueError('kwargs must be an iterable of an dicts')

        for i in range(0, n_elements_in_kwargs, 1):
            if kwargs[i] is None:
                kwargs[i] = {}
            else:
                try:
                    len(kwargs[0])
                except TypeError:
                    raise ValueError('kwargs must be an iterable of an dicts')

    if n_elements_in_args != n_elements_in_kwargs:
        if n_elements_in_args < n_elements_in_kwargs:
            if n_elements_in_args == 1:
                args = tuple([args[0] for i in range(0, n_elements_in_kwargs, 1)])
            elif n_elements_in_args > 1:
                raise ValueError('args cannot broadcast to kwargs')
            elif n_elements_in_args == 0:
                args = tuple([args for i in range(0, n_elements_in_kwargs, 1)])
            n_elements_in_args = n_elements_in_kwargs
        else:
            if n_elements_in_kwargs == 1:
                kwargs = tuple([kwargs[0] for i in range(0, n_elements_in_args, 1)])
            elif n_elements_in_kwargs > 1:
                raise ValueError('kwargs cannot broadcast to args')
            elif n_elements_in_kwargs == 0:
                kwargs = tuple([kwargs for i in range(0, n_elements_in_args, 1)])
            n_elements_in_kwargs = n_elements_in_args

    n_processes = n_elements_in_args

    # if n_workers is None:
    #     n_cpus = os.cpu_count()
    #     n_workers = min([n_cpus, n_processes])

    processes = [None for i in range(0, n_processes, 1)]  # type: list
    results = [None for i in range(0, n_processes, 1)]  # type: list

    executor = cf.ThreadPoolExecutor(
        max_workers=n_workers, thread_name_prefix='calapy.parallel_processes', initializer=None, initargs=())

    for i in range(0, n_processes, 1):

        args_i = args[i]
        kwargs_i = kwargs[i]
        processes[i] = executor.submit(func, *args_i, **kwargs_i)

    for i in range(0, n_processes, 1):
        results[i] = processes[i].result()

    executor.shutdown(wait=True, cancel_futures=False)

    return results
