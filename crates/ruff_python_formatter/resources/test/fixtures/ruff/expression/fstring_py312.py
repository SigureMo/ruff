# This file contains test cases only for cases where the logic tests for whether
# the target version is 3.12 or later. A user can have 3.12 syntax even if the target
# version isn't set.

# Quotes reuse
f"{'a'}"

# 312+, it's okay to change the outer quotes even when there's a debug expression using the same quotes
f'foo {10 + len("bar")=}'
f'''foo {10 + len("""bar""")=}'''

# 312+, it's okay to change the quotes here without creating an invalid f-string
f'{"""other " """}'
f'{"""other " """ + "more"}'
f'{b"""other " """}'
f'{f"""other " """}'


# Regression tests for https://github.com/astral-sh/ruff/issues/13935
f'{1: hy "user"}'
f'{1:hy "user"}'
f'{1: abcd "{1}" }'
f'{1: abcd "{'aa'}" }'
f'{1=: "abcd {'aa'}}'
f'{x:a{z:hy "user"}} \'\'\''

# Changing the outer quotes is fine because the format-spec is in a nested expression.
f'{f'{z=:hy "user"}'} \'\'\''


#  We have to be careful about changing the quotes if the f-string has a debug expression because it is inserted verbatim.
f'{1=: "abcd \'\'}'  # Don't change the outer quotes, or it results in a syntax error
f'{1=: abcd \'\'}'  # Changing the quotes here is fine because the inner quotes aren't the opposite quotes
f'{1=: abcd \"\"}'  # Changing the quotes here is fine because the inner quotes are escaped
# Don't change the quotes in the following cases:
f'{x=:hy "user"} \'\'\''
f'{x=:a{y:hy "user"}} \'\'\''
f'{x=:a{y:{z:hy "user"}}} \'\'\''
f'{x:a{y=:{z:hy "user"}}} \'\'\''

# This is fine because the debug expression and format spec are in a nested expression

f"""{1=: "this" is fine}"""
f'''{1=: "this" is fine}'''  # Change quotes to double quotes because they're preferred
f'{1=: {'ab"cd"'}}'  # It's okay if the quotes are in an expression part.
