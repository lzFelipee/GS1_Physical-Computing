import cv2

camera = cv2.VideoCapture(0)

detector = cv2.QRCodeDetector()

while True:

    sucesso, frame = camera.read()

    if not sucesso:
        break

    dados, pontos, _ = detector.detectAndDecode(frame)

    # Título do sistema
    cv2.putText(
        frame,
        "SPACE CARGO TRACKER",
        (20, 35),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 255, 255),
        2
    )

    if pontos is not None:

        pontos = pontos.astype(int)

        for i in range(len(pontos[0])):
            pt1 = tuple(pontos[0][i])
            pt2 = tuple(pontos[0][(i + 1) % len(pontos[0])])

            cv2.line(frame, pt1, pt2, (0, 255, 0), 3)

        if dados != "":

            print("QR Detectado:", dados)

            cv2.putText(
                frame,
                "CARGA IDENTIFICADA",
                (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.9,
                (0, 255, 0),
                2
            )

            cv2.putText(
                frame,
                f"ID: {dados}",
                (20, 120),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.9,
                (0, 255, 0),
                2
            )

        else:

            cv2.putText(
                frame,
                "QR CODE DETECTADO",
                (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.9,
                (0, 255, 255),
                2
            )

            cv2.putText(
                frame,
                "Lendo informacoes...",
                (20, 120),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.9,
                (0, 255, 255),
                2
            )

    else:

        cv2.putText(
            frame,
            "Aguardando QR Code...",
            (20, 80),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            (0, 0, 255),
            2
        )

    cv2.imshow("Space Cargo Tracker", frame)

    tecla = cv2.waitKey(1)

    if tecla == 27:
        break

camera.release()
cv2.destroyAllWindows()