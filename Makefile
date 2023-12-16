SRC_FILES=$(wildcard src/*.c)
HDR_FILES=$(wildcard src/*.h)

CC=gcc
CFLAGS=-Wall -Wextra -std=c17

LD=ld

TARGET_EXE=win32-subsystem

all: ${SRC_FILES} ${HDR_FILES}
	${CC} ${CFLAGS} ${SRC_FILES} ${HDR_FILES} -o ${TARGET_EXE}

run: all
	./${TARGET_EXE}

clean:
	rm -rf ${TARGET_EXE}
