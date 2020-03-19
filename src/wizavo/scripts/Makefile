#/*
# *	copyright (C) 2007 ICD Okada lab., Toyohashi University of Technology
# *
# *	FileName: Makefile
# *	Title: thread lib test program
# *	History: 
# * 		2008/10/31 [H.Takei]	#000#	Initial version
# * 		2018/07/06 [R.Mayumi]	#001#	32bitダウン対応 tcl8.6 ver.
# */


TARGET = wiz_client

CC = g++ -m32 #32bit版でのコンパイル
CFLAGS = -Wall -Werror -fPIC

SRCS = main.cpp
OBJS = $(SRCS:.ccp=.o)

LIBDIR = /usr/local/lib
INCDIR = /usr/local/include

LIBS = -L$(LIBDIR) -lwizvoice -lboost_system -ltcl8.6 -m32 #tclバージョンは適宜変更
INCS = -I$(INCDIR)


all: $(TARGET)

$(TARGET): $(OBJS)
	$(CC) $(CFLGS) -o $(TARGET) $(OBJS) $(INCS) $(LIBS)
	rm -rf *.o *~ *.wav wizvoice*.txt
	@echo "make success!"

%.o:%.cc
	$(CC) $(CFLAGS) -c $(INCS) $(LIBS) $<

clean:
	@echo "$(OBJS) clean"
	rm -rf $(TARGET) *.o *~ ./*.wav

