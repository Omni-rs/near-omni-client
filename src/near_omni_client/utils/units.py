USDC_DECIMALS = 6


def to_usdc_units(amount: float) -> int:
    return int(amount * (10**USDC_DECIMALS))
