-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 18-08-2024 a las 05:28:54
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `finalskate`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `accesorios`
--

CREATE TABLE `accesorios` (
  `id` int(11) NOT NULL,
  `nombre` varchar(60) NOT NULL,
  `precio` int(10) NOT NULL,
  `cantidad` int(10) NOT NULL,
  `tipo` varchar(60) NOT NULL,
  `stock_max` int(10) NOT NULL,
  `stock_min` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `accesorios`
--

INSERT INTO `accesorios` (`id`, `nombre`, `precio`, `cantidad`, `tipo`, `stock_max`, `stock_min`) VALUES
(1, 'Casco de Skate', 50, 20, 'Proteccion', 15, 5),
(2, 'Llave T', 300, 20, 'Herramienta', 20, 10);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ropa`
--

CREATE TABLE `ropa` (
  `id` int(11) NOT NULL,
  `nombre` varchar(60) NOT NULL,
  `precio` float NOT NULL,
  `cantidad` int(10) NOT NULL,
  `talla` varchar(5) NOT NULL,
  `material` varchar(16) NOT NULL,
  `stock_max` int(10) NOT NULL,
  `stock_min` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `ropa`
--

INSERT INTO `ropa` (`id`, `nombre`, `precio`, `cantidad`, `talla`, `material`, `stock_max`, `stock_min`) VALUES
(1, 'Camiseta', 200, 30, 'M', 'Algodon', 50, 10),
(2, 'Pantalon', 350, 25, 'L', 'Denim', 40, 5);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `skateboard`
--

CREATE TABLE `skateboard` (
  `id` int(11) NOT NULL,
  `nombre` varchar(60) NOT NULL,
  `precio` float NOT NULL,
  `cantidad` int(10) NOT NULL,
  `longitud` float NOT NULL,
  `stock_max` int(10) NOT NULL,
  `stock_min` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `skateboard`
--

INSERT INTO `skateboard` (`id`, `nombre`, `precio`, `cantidad`, `longitud`, `stock_max`, `stock_min`) VALUES
(1, 'BAKER', 1000, 11, 260, 20, 5),
(2, 'Santa Cruz', 800, 14, 240, 30, 10);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tenis`
--

CREATE TABLE `tenis` (
  `id` int(11) NOT NULL,
  `nombre` varchar(60) NOT NULL,
  `precio` float NOT NULL,
  `cantidad` int(10) NOT NULL,
  `talla` int(10) NOT NULL,
  `color` varchar(10) NOT NULL,
  `agujetas` varchar(5) NOT NULL,
  `stock_max` int(10) NOT NULL,
  `stock_min` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `tenis`
--

INSERT INTO `tenis` (`id`, `nombre`, `precio`, `cantidad`, `talla`, `color`, `agujetas`, `stock_max`, `stock_min`) VALUES
(1, 'Vans', 600, 16, 42, 'Negro', 'Si', 25, 5),
(2, 'Nike SB', 900, 10, 44, 'Blanco', 'si', 20, 5);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `apellido` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id`, `nombre`, `apellido`, `email`, `password`) VALUES
(1, 'Jonathan', 'Rios', 'jona@gmail.com', 'jona'),
(2, 'Axel', 'Sandoval', 'ax@gmail.com', '44'),
(3, 'Ricardo', 'Rios', 'ri@gmail.com', 'ri');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `accesorios`
--
ALTER TABLE `accesorios`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `ropa`
--
ALTER TABLE `ropa`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `skateboard`
--
ALTER TABLE `skateboard`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `tenis`
--
ALTER TABLE `tenis`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `correo` (`email`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `accesorios`
--
ALTER TABLE `accesorios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `ropa`
--
ALTER TABLE `ropa`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `skateboard`
--
ALTER TABLE `skateboard`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `tenis`
--
ALTER TABLE `tenis`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
