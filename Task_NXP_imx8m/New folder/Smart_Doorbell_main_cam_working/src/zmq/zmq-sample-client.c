#include <zmq.h>
#include <string.h>
#include <stdio.h>
#include <unistd.h>

int main (void)
{
    void *context = zmq_ctx_new ();
    void *requester = zmq_socket (context, ZMQ_REQ);
#if defined (LOCAL_HOST)
    zmq_connect (requester, "tcp://localhost:5555");
#else
    // host machine ip address 10.0.0.1
    zmq_connect (requester, "tcp://10.0.0.1:5555");
#endif

    char *buffer = "{\"command\":\"capture\"}";
    char rx_buffer[10000];
    printf ("Sending %s\n", buffer);
    zmq_send (requester, buffer, strlen(buffer), 0);
    zmq_recv (requester, rx_buffer, sizeof(rx_buffer), 0);
    printf ("Received %s\n", rx_buffer);

    zmq_close (requester);
    zmq_ctx_destroy (context);
    return 0;
}