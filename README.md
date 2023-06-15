# ansible-role-cs2modrewrite #

[![GitHub Build Status](https://github.com/cisagov/ansible-role-cs2modrewrite/workflows/build/badge.svg)](https://github.com/cisagov/ansible-role-cs2modrewrite/actions)
[![CodeQL](https://github.com/cisagov/ansible-role-cs2modrewrite/workflows/CodeQL/badge.svg)](https://github.com/cisagov/ansible-role-cs2modrewrite/actions/workflows/codeql-analysis.yml)

This Ansible role for downloading [cs2modrewrite](https://github.com/threatexpress/cs2modrewrite/blob/master/cs2modrewrite.py).

## Requirements ##

None.

## Role Variables ##

None.

<!--
| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| optional_variable | Describe its purpose. | `default_value` | No |
| required_variable | Describe its purpose. | n/a | Yes |
-->

## Dependencies ##

None.

## Example Playbook ##

Here's how to use it in a playbook:

```yaml
- hosts: all
  become: yes
  become_method: sudo
  tasks:
    - name: Install the cs2modrewrite tool
      ansible.builtin.include_role:
        name: cs2modrewrite
```

## Contributing ##

We welcome contributions!  Please see [`CONTRIBUTING.md`](CONTRIBUTING.md) for
details.

## License ##

This project is in the worldwide [public domain](LICENSE).

This project is in the public domain within the United States, and
copyright and related rights in the work worldwide are waived through
the [CC0 1.0 Universal public domain
dedication](https://creativecommons.org/publicdomain/zero/1.0/).

All contributions to this project will be released under the CC0
dedication. By submitting a pull request, you are agreeing to comply
with this waiver of copyright interest.

## Author Information ##

<<<<<<< HEAD
Heather Fetty - <heather.fetty@cisa.dhs.gov>
=======
First Last - <first.last@gwe.cisa.dhs.gov>
>>>>>>> b1e866deabc2408ffe58711e6a0f32446d183205
