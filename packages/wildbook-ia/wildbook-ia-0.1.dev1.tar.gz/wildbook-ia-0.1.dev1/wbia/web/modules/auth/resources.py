# -*- coding: utf-8 -*-
# pylint: disable=too-few-public-methods,invalid-name,bad-continuation
"""
Auth resources
--------------
"""

import logging

from flask_login import current_user, login_user, logout_user

from flask_restx_patched import Resource
from flask_restx_patched._http import HTTPStatus
from wbia.web.extensions import oauth2
from wbia.web.extensions.api import Namespace, api_v2
from wbia.web.extensions.api.parameters import PaginationParameters
from wbia.web.modules.users.models import User

from . import parameters, schemas
from .models import OAuth2Client, db
from .utils import create_session_oauth2_token, delete_session_oauth2_token

log = logging.getLogger(__name__)
api = Namespace('auth', description='Authentication')


def _generate_new_client(args):
    context = api.commit_or_abort(
        db.session, default_error_message='Failed to create a new OAuth2 client.'
    )
    with context:
        new_oauth2_client = OAuth2Client(user_guid=current_user.guid, **args)
        db.session.add(new_oauth2_client)
    return new_oauth2_client


@api.route('/sessions')
class OAuth2Sessions(Resource):
    """
    Login with Session.
    """

    @api.parameters(parameters.CreateOAuth2SessionParameters())
    @api.response(code=HTTPStatus.UNAUTHORIZED)
    @api.doc(id='create_oauth_session')
    def post(self, args):
        """
        Log-in via a new OAuth2 Session.
        """
        email = args['email']
        password = args['password']

        user = User.find(email=email, password=password)

        failure = None
        if user is not None:
            status = login_user(user, remember=False)

            if status:
                log.info('Logged in User via API: {!r}'.format(user))
                create_session_oauth2_token()
            else:
                failure = 'Account Disabled'
        else:
            failure = 'Account Not Found'

        if failure is None:
            response = {
                'success': True,
                'message': 'Session Created',
            }
            code = HTTPStatus.OK
        else:
            response = {
                'success': False,
                'message': failure,
            }
            code = HTTPStatus.UNAUTHORIZED

        return response, code

    @api.login_required(oauth_scopes=['auth:write'])
    def delete(self):
        """
        Log-out the active OAuth2 Session.
        """
        log.info('Logging out User via API: {!r}'.format(current_user))

        delete_session_oauth2_token()
        logout_user()

        response = {
            'success': True,
            'message': 'Session Deleted',
        }

        return response


@api.route('/clients')
@api.login_required(oauth_scopes=['auth:read'])
class OAuth2Clients(Resource):
    """
    Manipulations with OAuth2 clients.
    """

    # @api.parameters(parameters.ListOAuth2ClientsParameters())
    @api.parameters(PaginationParameters())
    @api.response(schemas.DetailedOAuth2ClientSchema(many=True))
    def get(self, args):
        """
        List of OAuth2 Clients.

        Returns a list of OAuth2 Clients starting from ``offset`` limited by
        ``limit`` parameter.
        """
        oauth2_clients = OAuth2Client.query
        oauth2_clients = oauth2_clients.filter(
            OAuth2Client.user_guid == current_user.guid,
            OAuth2Client.level != OAuth2Client.ClientLevels.confidential,
        )

        if oauth2_clients.count() == 0 and current_user.is_admin:
            default_scopes = list(
                api_v2.authorizations['oauth2_password']['scopes'].keys()
            )
            args_ = {
                'default_scopes': default_scopes,
            }
            _generate_new_client(args_)
            return self.get()

        return oauth2_clients.offset(args['offset']).limit(args['limit'])

    @api.login_required(oauth_scopes=['auth:write'])
    @api.parameters(parameters.CreateOAuth2ClientParameters())
    @api.response(schemas.DetailedOAuth2ClientSchema())
    @api.response(code=HTTPStatus.FORBIDDEN)
    @api.response(code=HTTPStatus.CONFLICT)
    @api.doc(id='create_oauth_client')
    def post(self, args):
        """
        Create a new OAuth2 Client.

        Essentially, OAuth2 Client is a ``guid`` and ``secret``
        pair associated with a user.
        """
        new_oauth2_client = _generate_new_client(args)
        return new_oauth2_client


@api.route('/tokens')
# @api.login_required(oauth_scopes=['auth:read'], locations=('headers', 'session', 'form', ))
class OAuth2Tokens(Resource):
    """
    Manipulations with OAuth2 clients.
    """

    @oauth2.token_handler
    def post(self):
        """
        This endpoint is for exchanging/refreshing an access token.

        Returns:
            response (dict): a dictionary or None as the extra credentials for
            creating the token response.
        """
        return None


@api.route('/revoke')
@api.login_required(oauth_scopes=['auth:read'])
class OAuth2Revoke(Resource):
    """
    Manipulations with OAuth2 clients.
    """

    # @api.login_required(oauth_scopes=['auth:write'])
    @oauth2.revoke_handler
    def post(self):
        """
        This endpoint allows a user to revoke their access token.
        """
        return None


@api.route('/recaptcha')
class ReCaptchaPublicServerKey(Resource):
    """
    Use signup form helper for recaptcha.
    """

    @api.response(schemas.ReCaptchaPublicServerKeySchema())
    def get(self):
        """
        Get recaptcha form keys.

        This endpoint must be used in order to get a server reCAPTCHA public key which
        must be used to receive a reCAPTCHA secret key for POST /<prefix>/users/ form.
        """
        response = {
            'recaptcha_public_key': 'recaptcha',
        }
        return response
