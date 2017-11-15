#pragma once

//#include "common.h"
//#include "config.h"

/* Max characters to encode a number */
#define str(s) #s
#define NUM_LINE_SIZE_BUF_STRING str(NUM_LINE_SIZE_BUF)
#define NUM_LINE_SIZE_BUF 8

/* default port */
#define DEFAULT_PORT 9999


#define CMD_SIZE 1
#define ARG_SIZE_SIZE NUM_LINE_SIZE_BUF

enum comm_cmd{
	GET_PAGE = 0,
	PRINT_ST
};

static char *comm_cmd_char[] = {
	"GET_PAGE",
	"PRINT_ST"
};

int comm_migrate(int nid);
int send_cmd(enum comm_cmd cmd, char *arg, int size);
int send_cmd_rsp(enum comm_cmd cmd, char *arg, int size, void* resp, int resp_size);