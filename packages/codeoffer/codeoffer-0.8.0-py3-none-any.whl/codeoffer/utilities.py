from codeoffer import exceptions


class Utilities:
    @staticmethod
    def handle_response(response):
        if response.status != 200:
            if response.status == 400:
                raise exceptions.BadRequestException(response.message)
            elif response.status == 409:
                raise exceptions.ConflictException(response.message)
            elif response.status == 403:
                raise exceptions.ForbiddenException(response.message)
            elif response.status == 500:
                raise exceptions.InternalServerException(response.message)
            elif response.status == 404:
                raise exceptions.NotFoundException(response.message)
            elif response.status == 408:
                raise exceptions.TimeoutException(response.message)
            elif response.status == 401:
                raise exceptions.UnauthorizedException(response.message)
            else:
                raise Exception(response.message)