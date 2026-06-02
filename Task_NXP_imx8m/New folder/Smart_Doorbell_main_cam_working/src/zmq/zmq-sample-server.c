#include <zmq.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <assert.h>
#include <cjson/cJSON.h>

int main (void)
{
    //  Socket to talk to clients
    void *context = zmq_ctx_new ();
    void *responder = zmq_socket (context, ZMQ_REP);
    int rc = zmq_bind (responder, "tcp://*:5555");
    assert (rc == 0);

    while (1) {
        char buffer [10000];
        zmq_recv (responder, buffer, sizeof(buffer), 0);
        printf ("Received %s\n", buffer);

        cJSON *json = cJSON_Parse(buffer);
        cJSON *command = cJSON_GetObjectItemCaseSensitive(json, "command");
        if (cJSON_IsString(command) && (command->valuestring != NULL))
        {
            printf("Received command \"%s\"\n", command->valuestring);
        }
        else
        {
            printf("invalid command");
        }
        cJSON_Delete(json);
        
        sleep (1);          //  Do some 'work'
        
        strcpy(buffer, "{\"response\":\"world\"}");
        printf("Sending reply %s\n", buffer);
        zmq_send (responder, buffer, sizeof(buffer), 0);
    }
    return 0;
}