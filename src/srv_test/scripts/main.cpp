/* for wizard voice */
#include <iostream>
#include <fstream>
#include <tcl/tcl.h>
#include <wizvoice.h>

/* for other */
#include <cstring>
#include <sstream>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#include <sys/types.h>

using namespace std;


#define BUF_SIZE 32


/*
 * Recieve a socket...
 */
string recvSocket( int sock ) {
    int data;
    char buf[ BUF_SIZE ];
    string str = "";
    do {
        memset(buf, 0, BUF_SIZE);
        data = read(sock, buf, BUF_SIZE);
        str += string(buf);
    } while(data == BUF_SIZE);
    
    /* error... */
    if (data == -1) {
        perror("error: Not connected...");
        exit(1);
    }

    /* error... */
    if (data == 0) {
        perror("error: Recieve an empty socket...");
        exit(1);
    }

    return str;
}


/*
 * Send a socket...
 */
int sendSocket( struct sockaddr_in *addr, int sock, string str ) {
    if( sock < 0 )
        cout << "Waiting access for two clients..." << "\n";
    else
        sendto( sock, str.c_str(), strlen(str.c_str()), 0, (struct sockaddr*)&addr, sizeof(addr) );

    return 1;
}


/*
 * Get port number...
 */
int getPort() {
    ifstream fin;
    fin.open("port.txt");
    int port;
    fin >> port;
    fin.close();
    return port;
}


/*
 * Get speaker...
 */
string getSpeaker() {
    ifstream fin;
    fin.open("speaker.txt");
    string speaker;
    fin >> speaker;
    fin.close();
    return speaker;
}


int main()
{
    struct sockaddr_in addr;
    int sock;

    int port = getPort();
    string speaker = getSpeaker();

    /* ソケットの作成 */
    sock = socket(AF_INET, SOCK_STREAM, 0);

    /* 接続先指定用構造体の準備 */
    addr.sin_family = AF_INET;
    addr.sin_port = htons( port );
    addr.sin_addr.s_addr = inet_addr("127.0.0.1");

    /* サーバに接続 */
    connect(sock, (struct sockaddr*)&addr, sizeof(addr));

    int cnt = 0;
    int CNTMAX = 10;

    while(1) {
        /* 受信したデータを表示 */
        string recv_str = recvSocket( sock );
        cout << "response > " << recv_str << "\n" << endl;

        /* wavファイル名 */
        ostringstream ss;
        ss << (cnt++) % CNTMAX;
        string wav = ss.str() + ".wav";
        cout << wav << "\n";

        /* create a wav file... */
        WizVoice::getInstance()->synthWaveOnlyFromKanji( (char*)recv_str.c_str(), (char*)wav.c_str(), (char*)speaker.c_str() );

        /* データを送信 */
        string send_str;
        send_str = wav;
        sendSocket( &addr, sock, send_str );
    }

    /* socketの終了 */
    close(sock);

    return 0;
}
