#include <cjson/cJSON.h>


cJSON * my_cJSON_Parse(const char *buffer)
{
    return cJSON_Parse(buffer);
}

cJSON * my_cJSON_GetObjectItemCaseSensitive(const cJSON *const object, const char *const string)
{
    return cJSON_GetObjectItemCaseSensitive(object, string);
}

cJSON_bool my_cJSON_IsString(const cJSON *const item)
{
    return cJSON_IsString(item);
}

void my_cJSON_Delete(cJSON *item)
{
    cJSON_Delete(item);
}