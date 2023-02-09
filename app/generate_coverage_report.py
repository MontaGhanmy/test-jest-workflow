from sys import argv
import xml.etree.ElementTree as ET

def generate_coverage_report(coverage_file):
    tree = ET.parse(coverage_file)
    root = tree.getroot()

    subfolder_totals = {}

    for file in root.iter("file"):
        path = file.get("path")
        subfolder = path.split("/")[-2]

        if subfolder not in subfolder_totals:
            subfolder_totals[subfolder] = [0, 0, 0, 0, 0]

        subfolder_totals[subfolder][0] += int(file.find("metrics").get("statements"))
        subfolder_totals[subfolder][1] += int(file.find("metrics").get("conditionals"))
        subfolder_totals[subfolder][2] += int(file.find("metrics").get("methods"))
        subfolder_totals[subfolder][3] += int(file.find("metrics").get("elements"))
        subfolder_totals[subfolder][4] += int(file.find("metrics").get("complexity"))

    report = "--------------|---------|----------|---------|---------|-------------------\n"
    report += "File          | % Stmts | % Branch | % Funcs | % Lines | Uncovered Line #s \n"
    report += "--------------|---------|----------|---------|---------|-------------------\n"

    for subfolder, metrics in subfolder_totals.items():
        report += f" {subfolder:<14} | {metrics[0]:<9} | {metrics[1]:<10} | {metrics[2]:<9} | {metrics[3]:<9} | {metrics[4]:<18} \n"

    report += "--------------|---------|----------|---------|---------|-------------------\n"

    return report

if __name__ == "__main__":
    print(generate_coverage_report(argv[1]))
