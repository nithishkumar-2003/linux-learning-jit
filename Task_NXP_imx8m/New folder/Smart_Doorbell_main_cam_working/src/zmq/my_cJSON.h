#include <cjson/cJSON.h>


cJSON * my_cJSON_Parse(const char *buffer);

cJSON * my_cJSON_GetObjectItemCaseSensitive(const cJSON *const object, const char *const string);

cJSON_bool my_cJSON_IsString(const cJSON *const item);

void my_cJSON_Delete(cJSON *item);