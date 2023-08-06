import requests

class SDKBuilder:
    """
    A base class for building SDKs that interact with a remote API.

    Provides methods for sending HTTP requests to the API and handling the response.

    Subclasses of this class can define specific endpoints and methods that are tailored
    to the API they are wrapping.

    Example usage:
        class MyAPI(SDKBuilder)
            host="https://example.com"
            get_user = client.GET("/users/{user_id}")
            
        client = MyAPI("my-secret-token")
        user_data = client.get_user(user_id=123)
    """
    def __init__(self, token):
        self.token = token

    def GET(endpoint):
        """
        Returns a function that sends an HTTP GET request to the specified endpoint
        using the host and token associated with the current instance.

        Parameters:
            - endpoint (str): the endpoint URL with optional format placeholders for
            the keyword arguments passed to the returned function.

        Returns:
            A function that takes arbitrary keyword arguments and sends an HTTP GET
            request to the URL constructed by combining the host, endpoint, and keyword
            arguments (formatted into the endpoint URL). If the response has a non-2xx status code,
            an exception is raised.
        """
        def request_func(self, **kwargs):
            """
            Sends an HTTP GET request to the endpoint with the given arguments.

            Parameters:
                - **kwargs: arbitrary keyword arguments to be formatted into the
                endpoint URL and sent as query parameters.

            Returns:
                The response content parsed as JSON.

            Raises:
                - requests.exceptions.HTTPError: if the response status code is
                not in the 2xx range.
            """
            url = f"{self.host}{endpoint.format(**kwargs)}"
            headers = {"Authorization": f"Bearer {self.token}"}
            response = requests.get(url, headers=headers, params=kwargs.get("params"))
            response.raise_for_status()
            return response.json()

        return request_func