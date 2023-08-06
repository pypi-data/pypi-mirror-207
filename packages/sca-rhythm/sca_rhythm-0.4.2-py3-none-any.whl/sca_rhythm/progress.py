import math
import time


class ExponentialWeightedAverage:
    def __init__(self, alpha: float = 0.9, start: float = 0):
        """
        Class for computing an exponential moving average.

        Args:
            alpha: The weight given to the most recent data.
            start: The starting value of the moving average.
        """
        self.s = start
        self.w = 1
        self.alpha = alpha

    def update(self, x: float) -> float:
        """
        Update the moving average with a new data point.

        Args:
            x: The new data point.

        Returns:
            The current value of the moving average.
        """
        self.s = self.alpha * self.s + (1 - self.alpha) * x
        self.w *= self.alpha
        return self.s / (1 - self.w)


class ETA:
    def __init__(self, alpha: float = 0.9):
        """
        Class for estimating the remaining time for a process to complete.

        Args:
            alpha: The weight given to the most recent progress update.
        """
        self.avg_rate = None
        self.progress = 0
        self.last_update_time = None
        self.moving_avg = ExponentialWeightedAverage(alpha=alpha, start=0)
        self.wt_avg_rate = None
        self.start_time = None

    def update(self, progress: float) -> float:
        """
        Update the estimated remaining time.

        Args:
            progress: The current progress, represented as a number between 0 and 1.

        Returns:
            The estimated remaining time in seconds.
        """
        if not 0 <= progress <= 1:
            return 0

        if self.start_time is None:
            self.start_time = time.perf_counter()

        if self.last_update_time is None:
            self.last_update_time = time.perf_counter()
            self.progress = progress
            return 1e100  # infinity; infinity is not compatible with JSON, use 1e100 instead

        diff = progress - self.progress
        self.progress = progress

        time_elapsed = time.perf_counter() - self.last_update_time
        self.last_update_time = time.perf_counter()

        curr_rate = diff / (1e-6 + time_elapsed)
        self.wt_avg_rate = self.moving_avg.update(curr_rate)

        # print(diff, time_elapsed, curr_rate, self.wt_avg_rate)

        if not math.isclose(self.wt_avg_rate, 0, rel_tol=1e-05, abs_tol=1e-08):
            remaining_time = (1 - progress) / self.wt_avg_rate
        else:
            remaining_time = 1e100  # infinity; infinity is not compatible with JSON, use 1e100 instead

        # calculate avg_rate of progress - fractions / second
        total_time_elapsed = time.perf_counter() - self.start_time
        self.avg_rate = progress / (1e-6 + total_time_elapsed)

        return remaining_time


class Progress:
    def __init__(self, name: str, total: int = None, units: str = None):
        self.name = name
        self.units = units
        self.total = total
        self.eta = ETA()

    def update(self, done: int):
        fraction_done = None
        time_remaining_sec = None
        wt_avg_rate = None
        avg_rate = None
        if self.total:
            fraction_done = done * 1.0 / self.total
            time_remaining_sec = self.eta.update(fraction_done)
            if self.eta.wt_avg_rate:
                wt_avg_rate = self.total * self.eta.wt_avg_rate
            if self.eta.avg_rate:
                avg_rate = self.total * self.eta.avg_rate
        return {
            'name': self.name,
            'fraction_done': fraction_done,
            'done': done,
            'total': self.total,
            'units': self.units,
            'time_remaining_sec': time_remaining_sec,
            'wt_avg_rate': wt_avg_rate,
            'avg_rate': avg_rate
        }


if __name__ == '__main__':
    import random

    total = 100
    done = 0
    p = Progress(name='test', units='number', total=total)
    start_time = time.perf_counter()

    p.update(done=0)
    while done < total:
        time.sleep(1)

        if done < 33:
            increment = random.randint(1, 4)
        elif done < 66:
            increment = random.randint(4, 6)
        else:
            increment = random.randint(6, 8)
        done = done + increment
        progress_obj = p.update(done=done)
        print(
            round(time.perf_counter() - start_time),
            increment,
            progress_obj['done'],
            round(progress_obj['fraction_done'], 2),
            round(progress_obj['time_remaining_sec'], 2),
            round(progress_obj['wt_avg_rate'], 2),
            round(progress_obj['avg_rate'], 2))

    time_elapsed = time.perf_counter() - start_time
    print('time_elapsed', time_elapsed, 'actual_avg_rate', total / time_elapsed)
