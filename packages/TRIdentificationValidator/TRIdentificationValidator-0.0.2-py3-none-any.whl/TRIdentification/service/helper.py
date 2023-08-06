invalid_identity_numbers = (
    '11111111111',
    '11111111110',
    '22222222220',
    '33333333330',
    '44444444440',
    '55555555550',
    '66666666660',
    '77777777770',
    '88888888880',
    '99999999990'
)


def IsValidIdentity(tckn: str) -> bool:
    if tckn in invalid_identity_numbers:
        return False
    if len(tckn) != 11:
        return False
    if not tckn.isdigit():
        return False
    if int(tckn[0]) == 0:
        return False
    identity_summary = (sum([int(tckn[i]) for i in range(0, 9, 2)]) * 7 - sum(
        [int(tckn[i]) for i in range(1, 9, 2)])) % 10
    if identity_summary != int(tckn[9]) or (sum([int(tckn[i]) for i in range(10)]) % 10) != int(tckn[10]):
        return False
    return True


def IsFromSyrian(tckn: str) -> bool:
    if tckn.startswith('99') or tckn.startswith('997'):
        return True
    return False
