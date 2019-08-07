
"""
Write a simple script to perform 5 consecutive HTTP calls to facebook.com every 30 seconds and
print response status code and response total time for each HTTP request to STDOUT. Additionally,
print average response time each five-request batch. This script can be written in any language, and
should run continuously until interrupted.

Create Docker container to run the script from previous step.
If possible, create as small an image as you can.

"""

import time
import requests

from utils import logger

import constants


logger = logger(__file__)


class HttpCalls(object):

    """
    This class has methods call_time_int and re_call. These methods
    run the request interval to facebook.com to find the response time,
    average response time of five-request batch and status codes for each
    HTTP request made.
    """
    def __init__(self, num):
        '''
        :param num: number of iterations
        '''
        self.num = num

    def call_time_int(self):
        """
        The call_time_int method runs the req_call method
        every 30 seconds until it is interrupted.
        :return: The results of the HTTP request calls to facebook.com
        """
        while True:
            self.process_response()
            time.sleep(30)

    @staticmethod
    def request_call():
        """
        The req_call method sends HTTP request call to URL
        :return: Response
        """
        try:
            response = requests.get(constants.FB_URL)
        except Exception as error:
            error_message = constants.ERROR_MESSAGE.format(error_message=str(error))
            logger.error(error_message)
            return False
        return response

    def process_response(self):
        """
        function to iterate on num variable and writes logs to STDOUT
        """
        resp_time = []
        for iteration in range(1, self.num+1):
            response = self.request_call()
            if not response:
                return
            response_time = response.elapsed.total_seconds()
            resp_time.append(response_time)
            status_code = response.status_code
            code_message = constants.STATUS_CODE.format(status_code=status_code, iter=iteration)
            response_time_message = \
                    constants.RESPONSE_TIME.format(response_time=response_time, iter=iteration)
            logger.info(code_message)
            logger.info(response_time_message)
        avg_response_time = sum(resp_time) / self.num
        avg_resp_message = \
                constants.AVG_RESPONSE_TIME.format(avg_response_time=avg_response_time,
                                                   iter=iteration)
        logger.info(avg_resp_message)


if __name__ == '__main__':

    OBJ = HttpCalls(5)
    OBJ.call_time_int()
