from fpdf import FPDF


def main():
    # Prompt user for their name
    name = input("Name: ")

    # Initialize A4 Portrait PDF
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.set_auto_page_break(auto=False)
    pdf.add_page()

    # 1. Top Header: "CS50 Shirtificate"
    pdf.set_font("Helvetica", "B", 46)
    pdf.cell(0, 50, "CS50 Shirtificate", align="C", new_x="LMARGIN", new_y="NEXT")

    # 2. Shirt Image: Centered horizontally (A4 width is 210mm, image width is 190mm -> x=10mm)
    pdf.image("shirtificate.png", x=10, y=70, w=190)

    # 3. Text on top of the shirt: "{Name} took CS50"
    pdf.set_font("Helvetica", "B", 26)
    pdf.set_text_color(255, 255, 255)  # White color text
    pdf.set_y(140)  # Moves cursor down to the chest area of the shirt
    pdf.cell(0, 10, f"{name} took CS50", align="C")

    # Output to shirtificate.pdf
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
