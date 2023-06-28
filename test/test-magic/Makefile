include ../../config/buildconf.makefile

CC=$(SNIPER_CC)

all: fft
	@echo
	@echo "Run 'make run' to run the program in the simulator"
	@echo

fft: fft.c Makefile
	$(CC) -o fft fft.c -lm -pthread $(SNIPER_LDFLAGS) $(SNIPER_CFLAGS)

run: fft
	../../run-sniper -n 2 -s magic_user --roi -- ./fft -p 2 -m 6

clean:
	rm -f fft sim.cfg sim.stats* *.log *.out
