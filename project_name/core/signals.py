"""Module with custom signals of the MyreksAPI project."""
from django import dispatch


post_soft_delete = dispatch.Signal(providing_args=['instance', 'using'])
