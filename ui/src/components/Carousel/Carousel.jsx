import React from "react";

// Import Swiper React components
import SwiperCore, { Pagination } from "swiper";
import { Swiper, SwiperSlide } from "swiper/react";
import "swiper/swiper.min.css";
import "swiper/components/pagination/pagination.min.css";
// Import Swiper styles
import { CardContainer } from "../../reusableComponents/Card";
SwiperCore.use([[Pagination]]);
export const Carousel = () => {
	return (
		<Swiper
			slidesPerView={1}
			pagination={{
				dynamicBullets: true,
			}}
		>
			<SwiperSlide>
				<CardContainer />
			</SwiperSlide>
			<SwiperSlide>
				<CardContainer />
			</SwiperSlide>
			<SwiperSlide>
				<CardContainer />
			</SwiperSlide>
		</Swiper>
	);
};
