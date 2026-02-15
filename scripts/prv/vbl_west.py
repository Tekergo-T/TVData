"""
 Copyright (c) 2023 Beáta Ungurán All rights reserved.
 Use of this source code is governed by a BSD-style
 license that can be found in the LICENSE file.
 """


def prv(brutto_gehalt, data_dict):
    """
    Calculate the social income and other related values based on the salary data and contribution rates.

    Args:
        brutto_gehalt (float): The gross salary.
        data_dict (dict): A dictionary containing the required data.

    Returns:
        Tuple: A tuple containing the following values:
            - sozialver_brutto (float): The gross salary which is used to determine the social security contributions.
            - strpflich_brutto (float): The taxable gross salary.
    """
    # Unpacking the data
    arbeitnehmeranteil = float(data_dict["arbeitnehmeranteil"]["value"]) / 100
    arbeitgeberanteil = float(data_dict["arbeitgeberanteil"]["value"]) / 100
    pauschal = float(data_dict["pauschal"]["value"]) 
    steuer_frei = float(data_dict["steuer_frei"]["value"])
    grenzbetrag = float(data_dict["grenzbetrag"]["value"])
    sozi_freibetrags = float(data_dict["sozi_freibetrags"]["value"])

    zurechnungs_grenze_2 = float(data_dict.get("zurechnungs_grenze_2", {"value": 1821.49})["value"])

    arbeitgeber_beitrag = arbeitgeberanteil * brutto_gehalt
    arbeitnehmer_beitrag = arbeitnehmeranteil * brutto_gehalt

    # Determining the taxable gross salary
    pauschal_rest = max(0, arbeitgeber_beitrag - steuer_frei)
    steuer_erhoehen = max(0, pauschal_rest - pauschal)
    strpflich_brutto = brutto_gehalt + max(0, steuer_erhoehen)

    # Determining the gross salary to be used to calculate the social security contributions
    zurechnungsbetrag_1 = max(0, min(steuer_frei, arbeitgeber_beitrag) +
                              min(pauschal, pauschal_rest) - grenzbetrag) + steuer_erhoehen

    zurechnungsbetrag_2 = max(0, (0.025 * min(brutto_gehalt, zurechnungs_grenze_2)) - sozi_freibetrags)

    sozialver_brutto = brutto_gehalt + \
        (zurechnungsbetrag_1 + zurechnungsbetrag_2)

    return sozialver_brutto, strpflich_brutto, arbeitnehmer_beitrag, arbeitgeber_beitrag


def main():
    # Example function call
    brutto_gehalt = 8600
    csv_data = {
        "arbeitnehmeranteil": {"value": 0.0181},
        "arbeitgeberanteil": {"value": 0.0549},
        "pauschal": {"value": 92.03},
        "steuer_frei": {"value": 219},
        "grenzbetrag": {"value": 100},
        "sozi_freibetrags": {"value": 13.30}
    }

    sozialver_brutto, strpflich_brutto, _, _ = prv(
        brutto_gehalt, csv_data)

    print("Social Gross Salary:", sozialver_brutto)
    print("Taxable Gross Salary:", strpflich_brutto)

