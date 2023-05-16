def prv(brutto_gehalt, data_dict):
    """
    Calculate the social income and other related values based on the salary data_dict and contribution rates.

    Args:
        brutto_gehalt (float): The gross salary.
        data_dict (dict): A dictionary containing the necessary parameters.

    Returns:
        Tuple: A tuple containing the following values:
            - sozialver_brutto (float): The gross salary used to determine the social security contributions.
            - strpflich_brutto (float): The taxable gross salary.
    """
    arbeitnehmeranteil = float(data_dict["arbeitnehmeranteil"]["value"])
    arbeitgeberanteil = float(data_dict["arbeitgeberanteil"]["value"])
    umlage = float(data_dict["umlage"]["value"])
    pauschal = float(data_dict["pauschal"]["value"])
    steuer_frei = float(data_dict["steuer_frei"]["value"])
    grenzbetrag = float(data_dict["grenzbetrag"]["value"])
    sozi_freibetrags = float(data_dict["sozi_freibetrags"]["value"])


    umlage_des_arbeitgebers_beitrag = umlage * brutto_gehalt
    arbeitnehmer_beitrag = arbeitnehmeranteil * brutto_gehalt
    arbeitgeber_beitrag = arbeitgeberanteil * brutto_gehalt

    # Determining the taxable gross salary
    pauschal_rest = umlage_des_arbeitgebers_beitrag - steuer_frei
    steuer_erhoehen = pauschal_rest - pauschal
    strpflich_brutto = brutto_gehalt + \
        max(0, steuer_erhoehen) - arbeitnehmer_beitrag

    # Determining the gross salary to be used to calculate the social security contributions
    zurechnungsbetrag_1 = max(0, min(steuer_frei, umlage_des_arbeitgebers_beitrag) +
                              min(pauschal, pauschal_rest) - grenzbetrag) + max(0, steuer_erhoehen)

    zurechnungsbetrag_2 = max(0, (brutto_gehalt / 100 - sozi_freibetrags))

    sozialver_brutto = strpflich_brutto + \
        (zurechnungsbetrag_1 + zurechnungsbetrag_2)

    return sozialver_brutto, strpflich_brutto, arbeitnehmer_beitrag, arbeitgeber_beitrag


# Example usage
salary_data = 12600

# Test dictionary containing the necessary parameters
data = {
    "arbeitnehmeranteil": {"value": 0.0425},
    "arbeitgeberanteil": {"value": 0.02},
    "umlage": {"value": 0.0106},
    "pauschal": {"value": 89.48},
    "steuer_frei": {"value": 219},
    "grenzbetrag": {"value": 100},
    "sozi_freibetrags": {"value": 13.30}
}

sozialver_brutto, strpflich_brutto, _, _ = prv(salary_data, data)

print("Social Gross Salary:", sozialver_brutto)
print("Taxable Gross Salary:", strpflich_brutto)
