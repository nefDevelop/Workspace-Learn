// Crear la instancia única de Log
// Pon tu nombre el constructor
const log = new Log("Neftalí Domínguez Urda"); // Pon aquí tu nombre

class Pez {
    constructor(nombre, imagenPez, xInicio, yInicio, tipoMovimiento, log) {
        this.nombre = nombre;
        this.x = xInicio;
        this.y = yInicio;
        this.tipoMovimiento = tipoMovimiento;
        this.direccionX = 1;
        this.direccionY = 1;
        this.elemento = document.createElement('img');
        this.elemento.src = imagenPez;
        this.elemento.className = 'pez';
        this.velocidad = 3;
        this.log = log;
        document.getElementById('pecera').appendChild(this.elemento);
        this.elemento.style.left = `${this.x}px`;
        this.elemento.style.top = `${this.y}px`;
        this.log.registrarPez(this);
    }

    mover() {
        switch (this.tipoMovimiento) {
            case 'horizontal':
                this.moverHorizontal();
                break;
            case 'zigzag':
                this.moverZigZag();
                break;
            case 'burbujaCascada':
                this.moverBurbujaCascada();
                break;
        }
        this.actualizarPosicion();
    }

    moverHorizontal() {
        this.x += this.velocidad * this.direccionX;

        if (this.x <= 0 || this.x >= 750) {
            this.direccionX *= -1;
            this.girarPez();
        }
    }

    moverZigZag() {
        this.x += this.velocidad * this.direccionX;
        this.y += Math.sin(this.x * 0.1) * 5 * this.direccionY;

        if (this.x <= 0 || this.x >= 750) {
            this.direccionX *= -1;
            this.girarPez();
        }
        if (this.y <= 0 || this.y >= 350) {
            this.direccionY *= -1;
        }
    }

    moverBurbujaCascada() {
        this.y += this.velocidad * this.direccionY;

        if (this.y <= 0 || this.y >= 350) {
            this.direccionY *= -1;
        }
    }

    girarPez() {
        this.elemento.style.transform = `scaleX(${this.direccionX})`;
    }

    actualizarPosicion() {
        this.elemento.style.left = `${this.x}px`;
        this.elemento.style.top = `${this.y}px`;
    }
}

const peces = [
    
];

function animar() {
    peces.forEach(pez => pez.mover());
    requestAnimationFrame(animar);
}

animar();