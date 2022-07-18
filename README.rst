**********************
Molecule Docker Plugin
**********************

.. image:: https://badge.fury.io/py/molecule-docker.svg
   :target: https://badge.fury.io/py/molecule-docker
   :alt: PyPI Package

.. image:: https://github.com/ansible-community/molecule-docker/workflows/tox/badge.svg
   :target: https://github.com/ansible-community/molecule-docker/actions

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/python/black
   :alt: Python Black Code Style

.. image:: https://img.shields.io/badge/license-MIT-brightgreen.svg
   :target: LICENSE
   :alt: Repository License

Molecule Docker Plugin is designed to allow use docker containers for
provisioning test resources.

Please note that this driver is currently in its early stage of development.

This plugin will function only if you also install `community.docker` ansible
collection. Keep in mind that this requires newer version of docker python
module which may not come with system-packaged versions of ansible like
Ubuntu ones.

Please do not file bugs towards molecule or this plugin if Ansible fails to
execute any docker modules (missing or incorrect versions of docker or requests
python modules). Instead file them on `community.docker <https://github.com/ansible-collections/community.docker>`_.

.. _get-involved:

Get Involved
============

* Join us in the ``#ansible-devtools`` channel on `Libera`_.
* Join the discussion in `molecule-users Forum`_.
* Join the community working group by checking the `wiki`_.
* Want to know about releases, subscribe to `ansible-announce list`_.
* For the full list of Ansible email Lists, IRC channels see the
  `communication page`_.

.. _`Libera`: https://web.libera.chat/?channel=#ansible-devtools
.. _`molecule-users Forum`: https://groups.google.com/forum/#!forum/molecule-users
.. _`wiki`: https://github.com/ansible/community/wiki/Molecule
.. _`ansible-announce list`: https://groups.google.com/group/ansible-announce
.. _`communication page`: https://docs.ansible.com/ansible/latest/community/communication.html

.. _faq:

FAQ
============

Q: How can I use Docker Context?

A: ``molecule-docker`` depends directly on
`community.docker.docker_container`_. Currently, `Docker Context` is not
supported, but as a workaround,
`docker_host in community.docker.docker_container`_ can be used to connect to
the Docker API.

.. _`community.docker.docker_container`: https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html
.. _`docker_host in community.docker.docker_container`: https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html#parameter-docker_host

.. _license:

License
=======

The `MIT`_ License.

.. _`MIT`: https://github.com/ansible/molecule/blob/main/LICENSE

The logo is licensed under the `Creative Commons NoDerivatives 4.0 License`_.

If you have some other use in mind, contact us.

.. _`Creative Commons NoDerivatives 4.0 License`: https://creativecommons.org/licenses/by-nd/4.0/
