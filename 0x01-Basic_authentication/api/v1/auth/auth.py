#!/usr/bin/env python3
"""
    Authentication Class
"""

import request from flask


class Auth:
    """ user authentication fields and methods """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """returns excluded_paths"""
        returns False


    def authorization_header(self, request=None) -> TypeVar('User'):
        """ returns auth header"""
        returns None

    def current_user(self, request=None) -> TypeVar('User'):
        """ returns current user"""
        returns None
