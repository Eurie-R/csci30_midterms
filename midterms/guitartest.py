#!/usr/bin/env python3

from guitarstring import GuitarString
from stdaudio import play_sample
import stdkeys
""" import picologging as logging """

if __name__ == '__main__':
    # initialize window
    """ logging.basicConfig(
        level=logging.DEBUG,
        filename="log.log",
        encoding="utf-8",
        filemode="a",
        format="{asctime} - {levelname}- {message}",
        style="{",
        datefmt="%Y-%m-%d %H:%M",
    ) """

    """ logging.info("Creating Window...") """
    stdkeys.create_window()

    keyboard = "q2we4r5ty7u8i9op-[=]"
    
    """ logging.info("Creating Keyboard...") """
    notes = [GuitarString(440 * (1.059463**(x-12))) for x in range(len(keyboard))] 
    for note in notes:
        """ logging.debug(note.capacity) """

    n_iters = 0
    while True:
        try:
            # it turns out that the bottleneck is in polling for key events
            # for every iteration, so we'll do it less often, say every 
            # 1000 or so iterations
            if n_iters == 1000:
                """ logging.debug(f'Polling keys - iter: {n_iters}...') """
                stdkeys.poll()
                n_iters = 0
            n_iters += 1

            # check if the user has typed a key; if so, process it
            if stdkeys.has_next_key_typed():
                key = stdkeys.next_key_typed()
                """ logging.debug(f'Key {key} pressed.') """
                try:
                    """ logging.debug(f'Plucking {key}.') """
                    notes[keyboard.index(key)].pluck()
                except:
                    pass
                # if key == 'a':
                #     string_A.pluck()
                # elif key == 'c':
                #     string_C.pluck()

            # compute the superposition of samples
            # sample = string_A.sample() + string_C.sample()
            sample = 0
            for note in notes:
                """ logging.debug(f'Sampling {note.capacity}.') """
                sample += note.sample()

            # play the sample on standard audio
            """ logging.info('Playing sample.') """
            play_sample(sample)

            # advance the simulation of each guitar string by one step
            for note in notes:
                """ logging.debug(f'Ticking {note.capacity}.') """
                note.tick()
        except:
            """ logging.error("Error...", exc_info=True) """