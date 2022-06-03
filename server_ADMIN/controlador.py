import scrap
import app

success = "EXITOSO, ELEMENTOS SCRAPEADOS:\n"

def main(prompt):
    registros = scrap.Scrap(prompt)
    for i in registros:
        try:
            app.db.session.add(i)
            app.db.session.commit()
        except:
            raise Exception("ERROR AGREGANDO RESULTADOS")
    return success